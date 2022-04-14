import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TwoRateThreeColorParameterFieldProps } from './two-rate-three-color-parameters';

export function TwoRateThreeColorBucketSSizeField(props: TwoRateThreeColorParameterFieldProps): ReactElement {
  const { twoRateThreeColorParameters, setTwoRateThreeColorParameters } = props;

  const twoRateThreeColorBucketSSize = useMemo(() => {
    return twoRateThreeColorParameters.bucketS_size || '';
  }, [twoRateThreeColorParameters]);

  const setTwoRateThreeColorBucketSSize = useSetNfvTeFunctionParameter('bucketS_size', setTwoRateThreeColorParameters);
  const onTwoRateThreeColorBucketSSizeChangeHandler = useChangeHandler(setTwoRateThreeColorBucketSSize);

  return (
    <FormInput
      label="Quantidade Inicial de Tokens no Bucket P"
      name="bucket-s-size"
      value={twoRateThreeColorBucketSSize}
      onChange={onTwoRateThreeColorBucketSSizeChangeHandler}
    />
  );
}
