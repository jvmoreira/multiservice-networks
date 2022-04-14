import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TwoRateThreeColorParameterFieldProps } from './two-rate-three-color-parameters';

export function TwoRateThreeColorBucketFMaxSizeField(props: TwoRateThreeColorParameterFieldProps): ReactElement {
  const { twoRateThreeColorParameters, setTwoRateThreeColorParameters } = props;

  const twoRateThreeColorBucketFMaxSize = useMemo(() => {
    return twoRateThreeColorParameters.bucketF_max_size || '';
  }, [twoRateThreeColorParameters]);

  const setTwoRateThreeColorBucketFMaxSize = useSetNfvTeFunctionParameter('bucketF_max_size', setTwoRateThreeColorParameters);
  const onTwoRateThreeColorBucketFMaxSizeChangeHandler = useChangeHandler(setTwoRateThreeColorBucketFMaxSize);

  return (
    <FormInput
      label="Tamanho Máximo do Bucket C"
      name="bucket-f-max-size"
      value={twoRateThreeColorBucketFMaxSize}
      placeholder="Valor em tokens"
      onChange={onTwoRateThreeColorBucketFMaxSizeChangeHandler}
    />
  );
}
