import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TwoRateThreeColorParameterFieldProps } from './two-rate-three-color-parameters';

export function TwoRateThreeColorBucketSMaxSizeField(props: TwoRateThreeColorParameterFieldProps): ReactElement {
  const { twoRateThreeColorParameters, setTwoRateThreeColorParameters } = props;

  const twoRateThreeColorBucketSMaxSize = useMemo(() => {
    return twoRateThreeColorParameters.bucketS_max_size || '';
  }, [twoRateThreeColorParameters]);

  const setTwoRateThreeColorBucketSMaxSize = useSetNfvTeFunctionParameter('bucketS_max_size', setTwoRateThreeColorParameters);
  const onTwoRateThreeColorBucketSMaxSizeChangeHandler = useChangeHandler(setTwoRateThreeColorBucketSMaxSize);

  return (
    <FormInput
      label="Tamanho Máximo do Bucket P"
      name="bucket-s-max-size"
      value={twoRateThreeColorBucketSMaxSize}
      placeholder="Valor em tokens"
      onChange={onTwoRateThreeColorBucketSMaxSizeChangeHandler}
    />
  );
}
